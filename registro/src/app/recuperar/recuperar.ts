import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators
} from '@angular/forms';

@Component({
  selector: 'app-recuperar',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './recuperar.html',
  styleUrl: './recuperar.css'
})
export class Recuperar {

  recuperarForm: FormGroup;
  isLoading = false;
  mensaje = '';

  constructor(private fb: FormBuilder) {
    this.recuperarForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]]
    });
  }

  isInvalid(): boolean {
    const email = this.recuperarForm.get('email');

    return !!(
      email &&
      email.invalid &&
      (email.dirty || email.touched)
    );
  }

  async onSubmit(): Promise<void> {

    if (this.recuperarForm.invalid) {
      this.recuperarForm.markAllAsTouched();
      return;
    }

    this.isLoading = true;
    this.mensaje = '';

    const email = this.recuperarForm.value.email;

    try {

      const respuesta = await fetch(
        'http://127.0.0.1:8000/api/recuperar/',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'text/plain'
          },
          body: JSON.stringify({
            email: email
          })
        }
      );

      const datos = await respuesta.json();

      if (respuesta.ok) {

        this.mensaje =
          'Si el correo está registrado, recibirás un enlace para recuperar tu contraseña.';

        this.recuperarForm.reset();

      } else {

        this.mensaje =
          datos.error || 'Ocurrió un error. Intenta nuevamente.';
      }

    } catch (error) {

      console.error('Error de conexión:', error);

      this.mensaje =
        'No fue posible conectar con el servidor.';

    } finally {

      this.isLoading = false;
    }
  }
}