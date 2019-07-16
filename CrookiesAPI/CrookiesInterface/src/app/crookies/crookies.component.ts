import { Component, OnInit } from '@angular/core';
import { CrookiesService } from '../shared/crookies.service';

@Component({
  selector: 'app-crookies',
  templateUrl: './crookies.component.html',
  styleUrls: ['./crookies.component.css']
})
export class CrookiesComponent implements OnInit {

  constructor(private service:CrookiesService) { }

  ngOnInit() {
    this.service.
  }

}
