import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-create-trade-lot',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './create-trade-lot.component.html',
  styleUrl: './create-trade-lot.component.scss'
})
export class CreateTradeLotComponent {
  ringName: string = '';
  goldPercentage: number = 0;
  silverPercentage: number = 0;
  bronzePercentage: number = 0;

  createTradeLot() {
    // Логіка створення нового лоту
    console.log(`Назва Кільця: ${this.ringName}, Золото: ${this.goldPercentage}%, Срібло: ${this.silverPercentage}%, Бронза: ${this.bronzePercentage}%`);
  }
}
