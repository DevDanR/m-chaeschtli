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
  recomendations: Product[] = []
  originalProduct: Product = {}

  products!: Product[];
  sliderValue!: number;
  cO2Value!: number;
  cO2ValueSlider!: number;
  bestValue!: number

  differenceValueCo2?: number

  constructor(private productService: ProductService) {}

  ngOnInit() {
    this.sliderValue = 5
    this.getData();
    this.getCo2Result()
    this.getRecomendations()
    this.getBestValue()
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
        this.sliderValue = res.food_waste_indicator_value
        this.getData()
      }
    )
  }

  getCo2Result() {
    this.productService.getCo2Result().subscribe(
      res => {
        this.cO2Value = res.customer_co2_footprint
        this.cO2ValueSlider = res.customer_co2_footprint / 30
      }
    )
  }

  getColor(keepability: number) {
    return keepability < 7;
  }

  getBestValue() {
    this.productService.getBestvalue().subscribe(
      res => this.bestValue = res.customer_co2_footprint_best
    )
  }

  getRecomendations() {
    this.productService.getProductRecomendations().subscribe(
      (res: any) => {
        this.originalProduct = res.product_recommendations[0][0]
        console.log(this.originalProduct)
        this.recomendations = res.product_recommendations[0][1]
      }
    )
  }
}

