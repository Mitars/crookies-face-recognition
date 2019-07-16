import { Injectable } from '@angular/core';
import { HttpClient } from 'selenium-webdriver/http';
import { Crookie } from './crookie.model';

@Injectable({
  providedIn: 'root'
})
export class CrookiesService {
  formData : Crookie;
  list : Crookie[];
  readonly rootURL = "https://localhost:44331/api";
  constructor(private http:HttpClient) { }
}

displayLogs(){
  this.http.get(this.rootURL + '/Crookie')
  .toPromise().then(res => this.list = res as Crookie[]);
}
