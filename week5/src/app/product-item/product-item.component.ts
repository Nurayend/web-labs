import { Component, OnInit} from '@angular/core';
import {categories} from '../categories';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})


export class ProductItemComponent implements OnInit {
  
  categories = categories;
  products;
  categoryIdFromRoute;
  constructor(
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap;
    this.categoryIdFromRoute = Number(routeParams.get('categoryId'));
    this.products = this.categories.find(category => category.id == this.categoryIdFromRoute).products;
  }

  onNotify():void {
    window.alert('You will be notified when the product goes on sale');
  }

  share(index) {
    this.products[index].share = 'https://telegram.me/share/url?url=' + this.products[index].link 
      + '&text=Hey, check out the ' + this.products[index].name + '!';
  }
  
  like(index) {
    if (this.products[index].isLiked === false) {
      this.products[index].like++;
      
    } else {
      this.products[index].like--;
    }
    this.products[index].isLiked = !this.products[index].isLiked;
  }

  remove(index) {
    this.products = this.products.filter(product => product.id !== index);
  }
}