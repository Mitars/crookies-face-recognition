import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CrookiesComponent } from './crookies.component';

describe('CrookiesComponent', () => {
  let component: CrookiesComponent;
  let fixture: ComponentFixture<CrookiesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CrookiesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CrookiesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
