//
//  HomeViewController.swift
//  NCRGymApp
//
//  Created by Desai, Saurav on 7/30/19.
//  Copyright © 2019 Desai, Saurav. All rights reserved.
//

import UIKit
import SwiftCharts

class HomeViewController: UIViewController {
    
    var chartView: BarsChart!

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        let chartConfig = BarsChartConfig(valsAxisConfig: ChartAxisConfig(from: 0, to: 900, by: 100))

        let frame = CGRect(x: 20, y: 150, width: self.view.frame.width - 40, height: 350)

        let chart = BarsChart(frame: frame, chartConfig: chartConfig, xTitle: "Day", yTitle: "Visits", bars: [
            ("M", 800),
            ("T", 500),
            ("W", 700),
            ("T", 400),
            ("F", 800)
            ], color: UIColor.cyan, barWidth: 30)
        self.view.addSubview(chart.view)
        self.chartView = chart
        
        // NOTE: this is just sample data to test the bars chart
    }


}

