import { Injectable } from '@angular/core';

@Injectable()
export class ProductService {
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

  getProductsSmall() {
    return Promise.resolve(this.getProductsData().slice(0, 10));
  }

  getProducts() {
    return Promise.resolve(this.getProductsData());
  }


  // getProductsWithOrdersSmall() {
  //   return Promise.resolve(this.getProductsWithOrdersData().slice(0, 10));
  // }
  //
  // getProductsWithOrders() {
  //   return Promise.resolve(this.getProductsWithOrdersData());
  // }
};
