import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient, HttpHeaders} from "@angular/common/http";

@Injectable()
export class ProductService {
  constructor(private http: HttpClient) {
  }
  getProductsData() {
    return [
      {
        id: '1000',
        code: 'f230fh0g3',
        name: 'Milch',
        image: 'bamboo-watch.jpg',
        price: 65,
        category: 'Produkte',
      },
      {
        id: '1001',
        code: 'nvklal433',
        name: 'Wurst',
        image: 'black-watch.jpg',
        price: 72,
        category: 'Produkte',
      }
    ];
  }

  getProducts(): Observable<any> {
    return this.http.get('http://localhost:105/customer_food_store')
  }

  eatProduct(id: string): Observable<any> {
    return this.http.post('http://localhost:105/get_food_waste_indicator_eaten', id)
  }

  trashProduct(id: string): Observable<any> {
    return this.http.post('http://localhost:105/get_food_waste_indicator_trashed', id)
  }

  getCo2Result(): Observable<any> {
    return this.http.get('http://localhost:105/get_customer_co2_footprint')
  }

  getBestvalue(): Observable<any> {
    return this.http.get('http://localhost:105/get_customer_co2_footprint_best')
  }

  getProductRecomendations(): Observable<any> {
    return this.http.get('http://localhost:105/product_recommendations')
  }
}

