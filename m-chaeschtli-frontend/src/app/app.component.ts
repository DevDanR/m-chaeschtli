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

  products!: Product[];
  sliderValue!: number;
  CO2Value!: number;

  constructor(private productService: ProductService) {}

  ngOnInit() {
    this.sliderValue = 5
    //this.productService.getProductsSmall().then((cars) => (this.products = cars));

    this.productService.getProducts().subscribe(
      res => {
        this.products = res.products_list
        console.log(res)
      }
    )
  }

  eatProduct(id: string) {
    this.productService.eatProduct(id).subscribe(
      res => {
        console.log("Result 1: " + res)
        this.sliderValue = res.food_waste_indicator_value
        this.productService.getProducts()
      })
  }

  trashProduct(id: string) {
    this.productService.trashProduct(id).subscribe(
      res => {
        console.log("Result 2: " + res)
        this.sliderValue = res.food_waste_indicator_value
        this.productService.getProducts()
      }
    )
  }

  getCo2Result() {
    this.productService.getCo2Result().subscribe(
      res => {
        console.log("Result 3: " + res)
        this.CO2Value = res
      }
    )
  }
}
