import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from "@angular/common/http";

import { AppComponent } from './app.component';
import { CrookiesComponent } from './crookies/crookies.component';
import { CrookiesService } from './shared/crookies.service';

@NgModule({
  declarations: [
    AppComponent,
    CrookiesComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [CrookiesService],
  bootstrap: [AppComponent]
})
export class AppModule { }
