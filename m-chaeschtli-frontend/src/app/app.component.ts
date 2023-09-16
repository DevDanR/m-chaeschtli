import {Component, OnInit} from '@angular/core';
import {ProductService} from "./service/product.service";
import {Product} from "./domain/product";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'm-chaeschtli-frontend';
  activeIndex: number | undefined;

  products!: [];
  sliderValue!: number;
  CO2Value!: number;

  constructor(private productService: ProductService) {}

  ngOnInit() {
    //this.productService.getProductsSmall().then((cars) => (this.products = cars));

    this.productService.getProducts().subscribe(
      res=> {
        this.products = res.products_list
        console.log(res)
      }
    )
  }

  eatProduct(id: string) {
    this.productService.eatProduct(id)
  }

  trashProduct(id: string) {
    this.productService.trashProduct(id)
  }
}
