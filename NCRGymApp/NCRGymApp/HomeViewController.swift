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

    @IBOutlet weak var uiChartView: UIView!
    
    var weekData: WeekData
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        let chartConfig = BarsChartConfig(valsAxisConfig: ChartAxisConfig(from: 0, to: 800, by: 200))

        let frame = CGRect(x: 0, y: 0, width: self.uiChartView.frame.width - 10, height: self.uiChartView.frame.height)

        let chart = BarsChart(frame: frame, chartConfig: chartConfig, xTitle: "Day", yTitle: "Visits", bars: [
            ("M", 800),
            ("T", 500),
            ("W", 700),
            ("T", 400),
            ("F", 800)
            ], color: UIColor.cyan, barWidth: 15)
        self.uiChartView.addSubview(chart.view)
        self.chartView = chart
        
        // TODO: retrieve actual data from server
    }
    
    func getData() {
        let weekDataRequest = WeekDataRequest()
        weekDataRequest.getData {[weak self] result in
            switch result {
            case .failure(let error):
                print(error)
            case .success(let weekData):
                self?.weekData = weekData
            }
        }
    }


}

