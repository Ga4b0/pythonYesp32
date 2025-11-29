import 'package:fl_chart/fl_chart.dart';
import 'package:flutter/material.dart';
import 'servicio_datos.dart';

class GraficaLineas extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Gráfica de Líneas")),
      body: ValueListenableBuilder<List<double>>(
        valueListenable: ServicioDatos.datos,
        builder: (context, datos, _) {
          if (datos.isEmpty) return Center(child: Text("Sin datos"));

          final maxY = datos.reduce((a, b) => a > b ? a : b) * 1.2;

          return Padding(
            padding: EdgeInsets.all(10),
            child: LineChart(
              LineChartData(
                minY: 0,
                maxY: maxY,
                lineBarsData: [
                  LineChartBarData(
                    spots: [
                      for (int i = 0; i < datos.length; i++)
                        FlSpot(i.toDouble(), datos[i])
                    ],
                    isCurved: true,
                    color: Colors.blue,
                    barWidth: 3,
                    dotData: FlDotData(show: true),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
