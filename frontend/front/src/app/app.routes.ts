import { Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { RegistryComponent } from './components/registry/registry.component';
import { UserHomeComponent } from './components/user-home/user-home.component';
import { AdminHomeComponent } from './components/admin-home/admin-home.component';
import { OwnerHomeComponent } from './components/owner-home/owner-home.component';

export const routes: Routes = [
    // { path: '', redirectTo: '/login', pathMatch: 'full' },
    { path: '', component: LoginComponent },
    { path: 'login', component: LoginComponent },
    { path: 'register', component: RegistryComponent },
    // { path: 'user-home', component: UserHomeComponent, canActivate: [AuthGuard], data: { role: 'User' } },
    // { path: 'admin-home', component: AdminHomeComponent, canActivate: [AuthGuard], data: { role: 'Admin' } },
    // { path: 'owner-home', component: OwnerHomeComponent, canActivate: [AuthGuard], data: { role: 'Owner' } },
    { path: 'user-home', component: UserHomeComponent},
    { path: 'admin-home', component: AdminHomeComponent},
    { path: 'owner-home', component: OwnerHomeComponent,},
    // { path: '**', redirectTo: '/login' }
];
