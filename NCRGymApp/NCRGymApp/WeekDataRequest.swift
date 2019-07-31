//
//  WeekDataRequest.swift
//  NCRGymApp
//
//  Created by Desai, Saurav on 7/31/19.
//  Copyright © 2019 Desai, Saurav. All rights reserved.
//

import Foundation


struct WeekDataRequest {
    let url: URL
    let apiKey = "7a6cd093b45790f7027ee"
    
    init() {
        
        // TODO: replace fake url and api key with real ones once backend is finished
        
        let urlString = "https://test-url.com/api/v1/gymdata?api_key=\(apiKey)"
        guard let url = URL(string: urlString) else {fatalError()}
        self.url = url
    }
}

