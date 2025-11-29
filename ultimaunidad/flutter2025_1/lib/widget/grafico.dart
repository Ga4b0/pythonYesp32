import 'package:fl_chart/fl_chart.dart';
import 'package:flutter/material.dart';
import 'dart:convert';
import 'dart:async';
import 'package:http/http.dart' as http;

class Grafico extends StatefulWidget {
  @override
  // ignore: no_logic_in_create_state
  State<StatefulWidget> createState() {
    return Clase();
  }
}

class Clase extends State<Grafico> {
  List<double> datosgrafica = [];
  bool cargando = true;
  Timer? timer;
  @override
  void initState() {
    super.initState();
    optenerDatos();
    timer = Timer.periodic(const Duration(seconds: 3), (timer) {
      optenerDatos();
    });
  }

  @override
  void dispose() {
    timer?.cancel();
    super.dispose();
  }

  Future optenerDatos() async {
    try {
      final url = Uri.parse("http://192.168.1.15:8000/api/sensores");
      final respuesta =
          await http.get(url).timeout(const Duration(seconds: 10));
      if (respuesta.statusCode == 200) {
        final dynamic datos = json.decode(respuesta.body);
        if (datos is List) {
          setState(() {
            final todosdatos = datos.map<double>((item) {
              final valorSensor = item['sensor1'];
              if (valorSensor is num) return valorSensor.toDouble();
              print("hola $valorSensor");
              return double.tryParse(item.toString()) ?? 0.0;
            }).toList();
            //print("hola $todosdatos,");
            datosgrafica = todosdatos.length > 10
                ? todosdatos.sublist(todosdatos.length - 5)
                : todosdatos;
            cargando = false;
          });
        }
      }
    } catch (e) {
      print('Error $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Graficas',
          style: TextStyle(
            color: Colors.white,
          ),
        ),
      ),
      body: cargando
          ? Center(child: CircularProgressIndicator())
          : Padding(
              padding: EdgeInsets.all(10),
              child: Column(
                children: [
                  Card(
                    elevation: 15,
                    child: Padding(
                      padding: EdgeInsets.all(5),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Column(children: [
                            Text("Datos a grafica"),
                            Text(
                              "Datos ${datosgrafica.length}",
                            ),
                          ]),
                          SizedBox(
                            width: 8,
                          ),
                          Column(
                            children: [
                              Text("Ultimo dato"),
                              Text(
                                "Datos ${datosgrafica.isNotEmpty ? datosgrafica.last.toStringAsFixed(1) : '0'}",
                              ),
                            ],
                          ),
                          Column(
                            children: [
                              Text("Primer dato"),
                              Text(
                                "Datos ${datosgrafica.isNotEmpty ? datosgrafica.first.toStringAsFixed(1) : '0'}",
                              ),
                            ],
                          )
                        ],
                      ),
                    ),
                  ),
                  Expanded(
                    child: BarChart(
                      BarChartData(
                        minY: 0,
                        maxY: datosgrafica.isNotEmpty
                            ? datosgrafica.reduce((a, b) => a > b ? a : b) * 1.2
                            : 100,
                        barGroups: datosgrafica.asMap().entries.map((entry) {
                          final indice = entry.key;
                          final valor = entry.value;
                          return BarChartGroupData(x: indice, barRods: [
                            BarChartRodData(
                              toY: valor,
                              color: Colors.amber,
                              width: 15,
                              borderRadius: BorderRadius.circular(5),
                            ),
                          ]);
                        }).toList(),
                        titlesData: FlTitlesData(
                          bottomTitles: AxisTitles(
                              sideTitles: SideTitles(
                                  showTitles: true,
                                  getTitlesWidget: (value, meta) {
                                    return Text('${value.toInt() + 1}');
                                  })),
                          leftTitles: AxisTitles(
                            sideTitles: SideTitles(
                              showTitles: true,
                              getTitlesWidget: (value, meta) {
                                return Text("${value.toInt()}");
                              },
                            ),
                          ),
                        ),
                        gridData: FlGridData(show: true),
                        borderData: FlBorderData(show: true),
                      ),
                    ),
                  ),
                  Expanded(
                    child: LineChart(
                      LineChartData(
                        minY: 0,
                        maxY: 100,
                        lineBarsData: [
                          LineChartBarData(
                            spots: [
                              for (int i = 0; i < datosgrafica.length; i++)
                                FlSpot(i.toDouble(), datosgrafica[i])
                            ],
                            isCurved: true,
                            color: Colors.red,
                            barWidth: 3,
                            dotData: FlDotData(show: false),
                          ),
                          LineChartBarData(
                            spots: [
                              for (int i = 0; i < datosgrafica.length; i++)
                                FlSpot(i.toDouble(), datosgrafica[i])
                            ],
                            isCurved: true,
                            color: Colors.blue,
                            barWidth: 3,
                            dotData: FlDotData(show: false),
                          ),
                        ],
                        titlesData: FlTitlesData(
                          bottomTitles: AxisTitles(
                            sideTitles: SideTitles(showTitles: false),
                          ),
                          leftTitles: AxisTitles(
                            sideTitles: SideTitles(showTitles: true),
                          ),
                        ),
                        gridData: FlGridData(show: true),
                        borderData: FlBorderData(show: true),
                      ),
                    ),
                  ),
                  Expanded(
                    child: PieChart(
                      PieChartData(
                        sections: () {
                          if (datosgrafica.isEmpty)
                            return <PieChartSectionData>[];

                          final total = datosgrafica.reduce((a, b) => a + b);

                          return datosgrafica.map<PieChartSectionData>((item) {
                            final valor = item;
                            final porcentaje =
                                total > 0 ? (valor / total) * 100 : 0;

                            return PieChartSectionData(
                              value: valor,
                              color: Colors.blue,
                              title: '${porcentaje.toStringAsFixed(1)}%',
                              radius: 50,
                              titleStyle: const TextStyle(
                                fontSize: 14,
                                fontWeight: FontWeight.bold,
                                color: Colors.white,
                              ),
                            );
                          }).toList();
                        }(),
                        centerSpaceRadius: 30,
                        sectionsSpace: 2,
                      ),
                    ),
                  ),
                ],
              ),
            ),
    );
  }
}

/*
Expanded(
                    child: LineChart(
                      LineChartData(
                        minY: 0,
                        maxY: datosgrafica.isNotEmpty
                            ? datosgrafica.reduce((a, b) => a > b ? a : b) * 1.2
                            : 100,
                        lineBarsData: [
                          LineChartBarData(
                            isCurved: true,
                            barWidth: 3,
                            color: Colors.blue,
                            spots: [
                              for (int i = 0; i < datosgrafica.length; i++)
                                FlSpot(i.toDouble(), datosgrafica[i]),
                            ],
                          ),
                        ],
                        titlesData: FlTitlesData(
                          bottomTitles: AxisTitles(
                            sideTitles: SideTitles(
                              showTitles: true,
                              getTitlesWidget: (value, meta) =>
                                  Text('${value.toInt() + 1}'),
                            ),
                          ),
                          leftTitles: AxisTitles(
                            sideTitles: SideTitles(
                              showTitles: true,
                              getTitlesWidget: (value, meta) =>
                                  Text('${value.toInt()}'),
                            ),
                          ),
                        ),
                        gridData: FlGridData(show: true),
                        borderData: FlBorderData(show: true),
                      ),
                    ),
                  ),
 */
