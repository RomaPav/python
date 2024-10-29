import { AfterViewInit, Component, ElementRef, Inject, OnDestroy, OnInit, PLATFORM_ID, Renderer2, ViewChild } from '@angular/core';
import { Chart, registerables  } from 'chart.js';
import { CommonModule } from '@angular/common';
import { isPlatformBrowser, isPlatformServer } from '@angular/common';
import { CoinService } from '../../services/coin.service';
import { TradeLotService } from '../../services/trade-lot.service';
import { PriceService } from '../../services/price.service';
import { BitService } from '../../services/bit.service';

@Component({
  selector: 'app-admin-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './admin-home.component.html',
  styleUrl: './admin-home.component.scss'
})
export class AdminHomeComponent implements OnInit, OnDestroy, AfterViewInit{
  public isBrowser: boolean;
  private coinService: CoinService
  private tradeLotService: TradeLotService
  visibleRings: any = [];
  cuurentGoldPrice = 0;
  cuurentSilverPrice = 0;
  cuurentBronzePrice = 0;
  private intervalId: any;
  user : any;

  constructor(private elementRef: ElementRef, 
      @Inject(PLATFORM_ID) platformId: Object,
      coinService: CoinService,
      traadeLotService: TradeLotService, 
      private priceService: PriceService,
      private bitService: BitService) {
    this.isBrowser = isPlatformBrowser(platformId);
    this.coinService = coinService
    this.tradeLotService = traadeLotService
    const user_storage = localStorage.getItem("user");
    this.user = user_storage ? JSON.parse(user_storage) : null;
  }

  

  ngOnInit() {
    this.getCoins()
  }
  ngAfterViewInit() {
    // this.createChart();
    this.intervalId = setInterval(() => {
      this.getPrice();
    }, 1000);
  }
  ngOnDestroy(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  }
  getCoins(){  
    this.tradeLotService.getStarted().subscribe({
      next: (response) => {
        this.visibleRings = response.data;
      },
      error: (error) => {
        console.error('Помилка входу', error);
      },
      complete: () => {
        console.log('Запит завершено адмін');
      }
    });
  } 

  startAuction(tradeLot: any) {
    tradeLot.trade_status = 'started';
    const bit ={
      "user_id": this.user.id,
      "trade_lot_id": tradeLot.id,
      "amount": 1
    }
    this.bitService.create(bit);
    this.tradeLotService.update(tradeLot).subscribe({
      next: (response) => {
        console.log(response);
        
      },
      error: (error) => {
        console.error('Помилка входу', error);
      },
      complete: () => {
        console.log('Запит завершено адмін');
      }
    });
  }

  endAuction(tradeLot: any){
    tradeLot.trade_status = 'closed';
    this.tradeLotService.update(tradeLot).subscribe({
      next: (response) => {
        console.log(response);
        this.getCoins()
      },
      error: (error) => {
        console.error('Помилка входу', error);
      },
      complete: () => {
        console.log('Запит завершено адмін');
      }
    });
  }

  getPrice(){
    this.priceService.getPrice(this.cuurentGoldPrice, this.cuurentSilverPrice, this.cuurentBronzePrice).subscribe({
      next: (response) => {
        this.cuurentGoldPrice = response.gold;
        this.cuurentSilverPrice = response.silver;
        this.cuurentBronzePrice = response.bronze;
      },
      error: (error) => {
        console.error('Помилка входу', error);
      },
      complete: () => {
        console.log('Запит завершено адмін');
      }
    });
  }

}
