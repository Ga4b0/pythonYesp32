import 'package:fl_chart/fl_chart.dart';
import 'package:flutter/material.dart';
import 'servicio_datos.dart';

class GraficaPie extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Gráfica Pie")),
      body: ValueListenableBuilder<List<double>>(
        valueListenable: ServicioDatos.datos,
        builder: (context, datos, _) {
          if (datos.isEmpty) return Center(child: Text("Sin datos"));

          final total = datos.fold<double>(0, (a, b) => a + b);

          return PieChart(
            PieChartData(
              centerSpaceRadius: 40,
              sectionsSpace: 2,
              sections: datos.map((valor) {
                final porcentaje = total > 0 ? (valor / total * 100) : 0;
                return PieChartSectionData(
                  value: valor,
                  color: Colors.blue,
                  title: "${porcentaje.toStringAsFixed(1)}%",
                  radius: 50,
                  titleStyle: TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                  ),
                );
              }).toList(),
            ),
          );
        },
      ),
    );
  }
}
