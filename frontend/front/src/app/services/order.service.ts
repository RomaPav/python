import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Order } from '../model/order';

@Injectable({
  providedIn: 'root'
})
export class OrderService {

  private apiUrl = "http://localhost:8080/order/"

  constructor(private http: HttpClient) { }

  getAll(){
    return this.http.get(this.apiUrl)
  }
  create(order: Order){
    return this.http.post(`${this.apiUrl}/`, order)
  }
  update(order: Order){
    return this.http.put(`${this.apiUrl}/`,order)
  }
  delete(id: Number){
    return this.http.delete(`${this.apiUrl}/${id}`)
  }
  getById(id: Number){
    return this.http.get(`${this.apiUrl}/${id}`)
  }
  getByUserId(id: Number){
    return this.http.get(`${this.apiUrl}/user-id/${id}`)
  }
}
