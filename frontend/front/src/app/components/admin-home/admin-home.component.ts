import { Component, ElementRef, Inject, PLATFORM_ID, Renderer2, ViewChild } from '@angular/core';
import { Chart, registerables  } from 'chart.js';
import { CommonModule } from '@angular/common';
import { isPlatformBrowser, isPlatformServer } from '@angular/common';
import { CoinService } from '../../services/coin.service';

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

  constructor(private elementRef: ElementRef, @Inject(PLATFORM_ID) platformId: Object, private renderer2: Renderer2, coinService: CoinService) {
    this.isBrowser = isPlatformBrowser(platformId);
    this.coinService = coinService
  }

  rings = [
    { name: 'Gold Ring', price: 1500, image: 'assets/gold_ring.jpg' },
    { name: 'Silver Ring', price: 700, image: 'assets/silver_ring.jpg' },
    { name: 'Platinum Ring', price: 2500, image: 'assets/platinum_ring.jpg' },
    { name: 'Palladium Ring', price: 2200, image: 'assets/palladium_ring.jpg' },
    { name: 'Titanium Ring', price: 1800, image: 'assets/titanium_ring.jpg' },
    { name: 'Copper Ring', price: 300, image: 'assets/copper_ring.jpg' },
    { name: 'Bronze Ring', price: 400, image: 'assets/bronze_ring.jpg' },
    { name: 'Steel Ring', price: 500, image: 'assets/steel_ring.jpg' }
  ];

  visibleRings: any = [];

  ngOnInit() {
    // this.visibleRings = this.rings.slice(0, 6);
    this.getCoins()
  }
  ngAfterViewInit() {
    this.createChart();
  }

  getCoins(){  
    this.coinService.getAll().subscribe({
      next: (response) => {
        this.visibleRings = response.data;
        console.log('Відповідь від сервера: фантастично юххууууу');
        // console.log(response);
      },
      error: (error) => {
        console.error('Помилка входу', error);
      },
      complete: () => {
        console.log('Запит завершено');
      }
    });
  } 


  loadMore() {
    const currentLength = this.visibleRings.length;
    const nextRings = this.rings.slice(currentLength, currentLength + 6);
    this.visibleRings = [...this.visibleRings, ...nextRings];
  }
  startAuction(ring: any) {
    alert(`Auction started for ${ring.name}`);
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
