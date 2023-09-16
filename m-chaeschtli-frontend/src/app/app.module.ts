import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {PanelModule} from "primeng/panel";
import {ButtonModule} from "primeng/button";
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import {TabViewModule} from "primeng/tabview";
import {TagModule} from "primeng/tag";
import {OrderListModule} from "primeng/orderlist";
import {ProductService} from "./service/product.service";
import {RippleModule} from "primeng/ripple";
import {SliderModule} from "primeng/slider";
import {FormsModule} from "@angular/forms";
import {HttpClient, HttpClientModule, HttpHandler} from "@angular/common/http";
import {StyleClassModule} from "primeng/styleclass";

@NgModule({
  declarations: [
    AppComponent
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        PanelModule,
        ButtonModule,
        BrowserAnimationsModule,
        TabViewModule,
        TagModule,
        OrderListModule,
        RippleModule,
        SliderModule,
        FormsModule,
        HttpClientModule,
        StyleClassModule
    ],
  providers: [ProductService, HttpClient],
  bootstrap: [AppComponent]
})
export class AppModule { }
