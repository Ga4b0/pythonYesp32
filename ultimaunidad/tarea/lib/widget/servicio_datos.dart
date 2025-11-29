import 'dart:async';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class ServicioDatos {
  static ValueNotifier<List<double>> datos = ValueNotifier([]);
  static Timer? timer;

  static void iniciar() {
    obtenerDatos();
    timer = Timer.periodic(Duration(seconds: 3), (_) => obtenerDatos());
  }

  static void detener() {
    timer?.cancel();
  }

  static Future<void> obtenerDatos() async {
    try {
      final url = Uri.parse("http://192.168.1.15:8000/api/sensores");
      final respuesta = await http.get(url).timeout(Duration(seconds: 10));

      if (respuesta.statusCode == 200) {
        final raw = json.decode(respuesta.body);

        if (raw is List) {
          List<double> nuevaLista = raw.map<double>((item) {
            final valor = item['sensor1'];
            if (valor is num) return valor.toDouble();
            return 0.0;
          }).toList();

          if (nuevaLista.length > 10) {
            nuevaLista = nuevaLista.sublist(nuevaLista.length - 10);
          }

          // 🔥 Notificar a los widgets
          datos.value = nuevaLista;
        }
      }
    } catch (e) {
      print("Error: $e");
    }
  }
}
