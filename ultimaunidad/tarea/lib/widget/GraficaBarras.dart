import 'package:fl_chart/fl_chart.dart';
import 'package:flutter/material.dart';
import 'servicio_datos.dart';

class GraficaBarras extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Gráfica de Barras")),
      body: ValueListenableBuilder<List<double>>(
        valueListenable: ServicioDatos.datos,
        builder: (context, datos, _) {
          if (datos.isEmpty) return Center(child: Text("Sin datos"));

          final maxY = datos.reduce((a, b) => a > b ? a : b) * 1.2;

          return Padding(
            padding: EdgeInsets.all(10),
            child: BarChart(
              BarChartData(
                minY: 0,
                maxY: maxY,
                barGroups: datos.asMap().entries.map((e) {
                  final i = e.key;
                  final val = e.value;
                  return BarChartGroupData(x: i, barRods: [
                    BarChartRodData(
                      toY: val,
                      color: Colors.amber,
                      width: 15,
                      borderRadius: BorderRadius.circular(5),
                    ),
                  ]);
                }).toList(),
              ),
            ),
          );
        },
      ),
    );
  }
}
