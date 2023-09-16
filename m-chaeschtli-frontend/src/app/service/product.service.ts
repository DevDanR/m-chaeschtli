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

  getProductsMini() {
    return Promise.resolve(this.getProductsData().slice(0, 5));
  }

  getProducts(): Observable<any> {
    return this.http.get('http://localhost:105/customer_purchases')
  }

  eatProduct(id: string) {
    return this.http.post('http://localhost:105/get_food_waste_indicator_eaten', id)
  }

  trashProduct(id: string) {
    return this.http.post('http://localhost:105/get_food_waste_indicator_trashed', id)
  }
}


export class Product {
  id?: string;
  code?: string;
  name?: string;
  price?: number;
  category?: string;
  image?: string;
}
