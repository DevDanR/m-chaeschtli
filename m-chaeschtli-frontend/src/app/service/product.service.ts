import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

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

  // getProductsSmall() {
  //   return Promise.resolve(this.getProductsData().slice(0, 10));
  // }

  // getProducts() {
  //   return Promise.resolve(this.getProductsData());
  // }

  getProducts(): Observable<any> {
    return this.http.get('http://localhost:105/customer_purchases')
  }


  // getProductsWithOrdersSmall() {
  //   return Promise.resolve(this.getProductsWithOrdersData().slice(0, 10));
  // }
  //
  // getProductsWithOrders() {
  //   return Promise.resolve(this.getProductsWithOrdersData());
  // }
  eatProduct(id: string) {
    console.log("Id to be: " + id)
    return this.http.post('this.localhost:105/get_food_waste_indicator_eaten', id)
  }

  trashProduct(id: string) {
    console.log("Id to be" + id)
    return this.http.post('this.localhost:105/get_food_waste_indicator_trashed', id)
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
