import { Component, OnInit } from '@angular/core';
import { CrookieService } from '../shared/crookie.service';

@Component({
  selector: 'app-crookies',
  templateUrl: './crookies.component.html',
  styleUrls: ['./crookies.component.css']
})
export class CrookiesComponent implements OnInit {

  constructor(private service : CrookieService) { }

  ngOnInit() {
    this.service.refreshLogs();
  }

}
