import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CrookieListComponent } from './crookie-list.component';

describe('CrookieListComponent', () => {
  let component: CrookieListComponent;
  let fixture: ComponentFixture<CrookieListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CrookieListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CrookieListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
