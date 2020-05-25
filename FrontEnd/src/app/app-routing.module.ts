import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { ProfileComponent } from './profile/profile.component';
import { MenuComponent } from './menu/menu.component';
import { EvidenciasComponent } from './evidencias/evidencias.component';
import { GruposComponent } from './grupos/grupos.component';
import { ConfigComponent } from './config/config.component';


const routes: Routes = [
  {
    path: '',
    redirectTo: '/login',
    pathMatch: 'full'
  },
  {
    path: 'login',
    component: LoginComponent,
  },
  {
    path: 'inicio',
    component: SidebarComponent,
    children:[
      {
        path: '',
        component: MenuComponent,
      },
      {
        path: 'menu',
        component: MenuComponent,
      },
      {
        path: 'profile',
        component: ProfileComponent,
      },
      {
        path: 'evidencias',
        component: EvidenciasComponent,
      },
      {
        path: 'grupos',
        component: GruposComponent,
      },
      {
        path: 'config',
        component: ConfigComponent,
      }

    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
