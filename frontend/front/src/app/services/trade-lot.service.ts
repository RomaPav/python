import { Injectable } from '@angular/core';
import { TradeLot } from '../model/trade-lot';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TradeLotService {
  private apiUrl = "http://localhost:8080/trade-lot/"

  constructor(private http: HttpClient) { }

  getAll(){
    return this.http.get(this.apiUrl)
  }
  create(tradeLot: TradeLot){
    return this.http.post(`${this.apiUrl}/`, tradeLot)
  }
  update(tradeLot: TradeLot){
    return this.http.put(`${this.apiUrl}/`,tradeLot)
  }
  delete(id: Number){
    return this.http.delete(`${this.apiUrl}/${id}`)
  }
  getById(id: Number){
    return this.http.get(`${this.apiUrl}/${id}`)
  }
  getByUserId(id: Number){
    return this.http.get(`${this.apiUrl}/coin-id/${id}`)
  }
}
