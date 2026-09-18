import { Routes } from '@angular/router';
import { Register } from './register/register';
import { Recuperar } from './recuperar/recuperar';

export const routes: Routes = [
  {
    path: '',
    component: Register
  },
  {
    path: 'recuperar',
    component: Recuperar
  }
];