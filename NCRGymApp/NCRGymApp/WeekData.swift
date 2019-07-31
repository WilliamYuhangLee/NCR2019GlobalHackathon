//
//  WeekData.swift
//  NCRGymApp
//
//  Created by Desai, Saurav on 7/31/19.
//  Copyright © 2019 Desai, Saurav. All rights reserved.
//

import Foundation

/**
 {
    "Monday": 800,
    "Tuesday": 600,
    "Wednesday": 700,
    "Thursday": 700,
    "Friday": 800
 }
 **/

struct WeekData: Decodable {
    var monday: Int
    var tuesday: Int
    var wednesday: Int
    var thursday: Int
    var friday: Int
}
