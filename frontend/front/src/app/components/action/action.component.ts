import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BitService } from '../../services/bit.service';
import { CoinService } from '../../services/coin.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-action',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './action.component.html',
  styleUrl: './action.component.scss'
})
export class ActionComponent implements OnInit, OnDestroy {
  auctionId: string | null | undefined;
  tradeInfo: any;
  coin: any = 0;
  amount: number = 0;
  private intervalId: any;

  constructor(private route: ActivatedRoute, private bitService: BitService, private coinService: CoinService) { }

  ngOnInit(): void {
    this.auctionId = this.route.snapshot.paramMap.get('id');
    if (this.auctionId){
      this.getTradeInfo(parseInt(this.auctionId));
    }
    this.intervalId = setInterval(() => {
      if (this.auctionId){
        this.getTradeInfo(parseInt(this.auctionId));
      }
    }, 10000);

  }

  ngOnDestroy(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  }

  getTradeInfo(id: Number){  
    this.bitService.getByTradeLotId(id).subscribe({
      next: (response) => {
        this.tradeInfo = response.data;
        this.amount = this.tradeInfo.amount
        this.getCoin(parseInt(this.tradeInfo.trade_lot.coin_id));
      },
      error: (error) => {
        console.error('Помилка входу', error);
      },
      complete: () => {
        console.log('Запит завершено');
      }
    });
  } 


  getCoin(id: Number){  
    this.coinService.getById(id).subscribe({
      next: (response) => {
        this.coin = response.data;
      },
      error: (error) => {
        console.error('Помилка входу', error);
      },
      complete: () => {
        console.log('Запит завершено');
      }
    });
  }
  
  checkAmount(){
    if(this.amount < 0){
      this.amount = 0;
    }
  }

  onAmountChange(event: Event) {
    const input = event.target as HTMLInputElement; 
    const value = parseFloat(input.value); 

    if (value >= 0) {
      this.amount = value;
    } else {
      this.amount = 0; 
      input.value = '0'; 
    }
  }

  updateAmount(){
    if(this.amount < this.tradeInfo.amount){
      const user_storage = localStorage.getItem("user");
      const user = user_storage ? JSON.parse(user_storage) : null;
      this.tradeInfo.user_id = user.id
      this.amount = this.tradeInfo.amount;
      console.log(this.tradeInfo)
      this.bitService.update(this.tradeInfo).subscribe({
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
  }

}
