import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from "@angular/common/http";


import { AppComponent } from './app.component';
import { CrookiesComponent } from './crookies/crookies.component';
import { CrookieListComponent } from './crookies/crookie-list/crookie-list.component';
import { CrookieService } from './shared/crookie.service';

@NgModule({
  declarations: [
    AppComponent,
    CrookiesComponent,
    CrookieListComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [CrookieService],
  bootstrap: [AppComponent]
})
export class AppModule { }
