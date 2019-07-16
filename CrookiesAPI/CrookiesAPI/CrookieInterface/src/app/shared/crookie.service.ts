import { Injectable } from '@angular/core';
import { Crookie } from './crookie.model';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class CrookieService {

  formData : Crookie;
  readonly rootURL = "https://localhost:44331/api";
  list : Crookie[];

  constructor(private http : HttpClient) { }

  refreshLogs(){
    this.http.get(this.rootURL + '/Crookie')
    .toPromise().then(res => this.list = res as Crookie[]);
  }
}
