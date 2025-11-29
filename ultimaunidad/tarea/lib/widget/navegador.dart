import 'package:flutter/material.dart';
import 'servicio_datos.dart';
import 'GraficaBarras.dart';
import 'GraficaLineas.dart';
import 'GraficaPie.dart';

class navegador extends StatefulWidget {
  @override
  State<navegador> createState() => _navegador();
}

class _navegador extends State<navegador> {
  int paginaActual = 0;

  @override
  void initState() {
    super.initState();
    ServicioDatos.iniciar(); // inicia el timer y la obtención de datos
  }

  @override
  void dispose() {
    ServicioDatos.detener();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final paginas = [
      GraficaBarras(),
      GraficaLineas(),
      GraficaPie(),
    ];

    return Scaffold(
      body: paginas[paginaActual],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: paginaActual,
        onTap: (i) => setState(() => paginaActual = i),
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.bar_chart), label: 'Barras'),
          BottomNavigationBarItem(
              icon: Icon(Icons.show_chart), label: 'Líneas'),
          BottomNavigationBarItem(icon: Icon(Icons.pie_chart), label: 'Pie'),
        ],
      ),
    );
  }
}
