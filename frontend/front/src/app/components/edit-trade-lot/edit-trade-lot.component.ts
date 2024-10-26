import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-edit-trade-lot',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './edit-trade-lot.component.html',
  styleUrl: './edit-trade-lot.component.scss'
})
export class EditTradeLotComponent {
  tradeLot = { name: 'Золотий Перстень' }; // Приклад назви лоту
  tradeStatuses = ['active', 'inactive', 'closed'];
  selectedTradeStatus: string = '';

  saveTradeLot() {
    // Логіка збереження лоту
    console.log(`Лот: ${this.tradeLot.name}, Статус: ${this.selectedTradeStatus}`);
  }
}
