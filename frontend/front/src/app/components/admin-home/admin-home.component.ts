import { Component, ElementRef, Inject, PLATFORM_ID, Renderer2, ViewChild } from '@angular/core';
import { Chart, registerables  } from 'chart.js';
import { CommonModule } from '@angular/common';
import { isPlatformBrowser, isPlatformServer } from '@angular/common';
import { CoinService } from '../../services/coin.service';
import { TradeLotService } from '../../services/trade-lot.service';

@Component({
  selector: 'app-admin-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './admin-home.component.html',
  styleUrl: './admin-home.component.scss'
})
export class AdminHomeComponent {
  public isBrowser: boolean;
  private coinService: CoinService
  private tradeLotService: TradeLotService
  visibleRings: any = [];

  constructor(private elementRef: ElementRef, @Inject(PLATFORM_ID) platformId: Object, private renderer2: Renderer2, coinService: CoinService, traadeLotService: TradeLotService) {
    this.isBrowser = isPlatformBrowser(platformId);
    this.coinService = coinService
    this.tradeLotService = traadeLotService
  }

  

  ngOnInit() {
    // this.visibleRings = this.rings.slice(0, 6);
    this.getCoins()
  }
  ngAfterViewInit() {
    this.createChart();
  }

  getCoins(){  
    this.tradeLotService.getStarted().subscribe({
      next: (response) => {
        this.visibleRings = response.data;
        // console.log(response.data);
      },
      error: (error) => {
        console.error('Помилка входу', error);
      },
      complete: () => {
        console.log('Запит завершено');
      }
    });
  } 

  getPrice(){
    
  }

  startAuction(tradeLot: any) {
    tradeLot.trade_status = 'started';
    this.tradeLotService.update(tradeLot).subscribe({
      next: (response) => {
        console.log(response);
      },
      error: (error) => {
        console.error('Помилка входу', error);
      },
      complete: () => {
        console.log('Запит завершено');
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
        console.log('Запит завершено');
      }
    });
  }


  createChart() {
    Chart.register(...registerables); 
    const ctx = this.elementRef.nativeElement.querySelector('#priceChart');

    if (ctx) {
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['January', 'February', 'March', 'April', 'May', 'June'],
          datasets: [{
            label: 'Cold',
            data: [1500, 1550, 1600, 1580, 1620, 1650],
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            fill: false
          },
          {
            label: 'Silver',
            data: [1510, 1450, 1120, 1500, 1200, 1610],
            borderColor: 'rgba(175, 192, 192, 1)',
            borderWidth: 2,
            fill: false
          },
          {
            label: 'Bronse',
            data: [2000, 1550, 1630, 1581, 1450, 1050],
            borderColor: 'rgba(75, 102, 192, 1)',
            borderWidth: 2,
            fill: false
          }
        ]
        },
        options: {
          responsive: true,
          scales: {
            x: {
              display: true,
              title: {
                display: true,
                text: 'Month'
              }
            },
            y: {
              display: true,
              title: {
                display: true,
                text: 'Price (USD)'
              }
            }
          }
        }
      });
    }
  }
}
