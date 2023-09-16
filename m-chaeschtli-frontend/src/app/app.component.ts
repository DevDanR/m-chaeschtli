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
  recomendations = []

  products!: Product[];
  sliderValue!: number;
  cO2Value!: number;

  constructor(private productService: ProductService) {}

  ngOnInit() {
    this.sliderValue = 5
    this.getData();
  }

  getData() {
    this.productService.getProducts().subscribe(
      res => {
        this.products = res.products_list.sort((a: { keepability: number; }, b: { keepability: number; }) =>
          a.keepability - b.keepability)
      }
    )
  }

  eatProduct(id: string) {
    this.productService.eatProduct(id).subscribe(
      res => {
        console.log("Result 1: " + res)
        this.sliderValue = res.food_waste_indicator_value
        this.getData()
      })
  }

  trashProduct(id: string) {
    this.productService.trashProduct(id).subscribe(
      res => {
        console.log("Result 2: " + res)
        this.sliderValue = res.food_waste_indicator_value
        this.getData()
      }
    )
  }

  getCo2Result() {
    this.productService.getCo2Result().subscribe(
      res => {
        console.log("Result 3: " + res)
        this.cO2Value = res
      }
    )
  }

  getColor(keepability: number) {
    console.log(keepability)
    return keepability < 7;
  }

  getBestValue() {
    this.productService.getBestvalue().subscribe(
      res => this.cO2Value = res
    )
  }

  getRecomendations() {
    this.productService.getProductRecomendations().subscribe(
      (res: []) => { this.recomendations = res}
    )
  }
}
