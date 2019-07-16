import { Component, OnInit } from '@angular/core';
import { CrookieService } from 'src/app/shared/crookie.service';

@Component({
  selector: 'app-crookie-list',
  templateUrl: './crookie-list.component.html',
  styleUrls: ['./crookie-list.component.css']
})
export class CrookieListComponent implements OnInit {

  constructor(private service : CrookieService) { }

  ngOnInit() {
    this.service.refreshLogs();
  }

}
