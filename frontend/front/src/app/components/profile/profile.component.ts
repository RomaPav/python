import { Component, OnDestroy, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.scss'
})
export class ProfileComponent {
  user = {
    fullName: 'Іван Іванов',
    username: 'ivan.ivanov',
    email: 'ivan@example.com',
    password: ''
  };

  originalUser = { ...this.user }; 
  hasChanges = false;

  onChanges() {
    this.hasChanges = JSON.stringify(this.user) !== JSON.stringify(this.originalUser);
  }

  saveChanges() {
    this.originalUser = { ...this.user }; 
    this.hasChanges = false; 
    alert('Зміни збережено!'); 
  }
}
