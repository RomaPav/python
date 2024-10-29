import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PriceService {

  private apiUrl = "http://localhost:8090/price/"

  constructor(private http: HttpClient) { }

  getPrice(goldPrice:number, silverPrice: number, bronzePrice: number) :Observable<any>{
    return this.http.get(`${this.apiUrl}${goldPrice}/${silverPrice}/${bronzePrice}`)
  }
}
