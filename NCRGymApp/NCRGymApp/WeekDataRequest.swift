//
//  WeekDataRequest.swift
//  NCRGymApp
//
//  Created by Desai, Saurav on 7/31/19.
//  Copyright © 2019 Desai, Saurav. All rights reserved.
//

import Foundation


enum DataError: Error {
    case noDataAvailable
    case canNotProcessData
}

struct WeekDataRequest {
    let url: URL
    
    init() {
        
        // TODO: replace fake url and api key with real ones once backend is finished
        
        let urlString = "http://127.0.0.1:5000/stats/week"
        guard let url = URL(string: urlString) else {fatalError()}
        self.url = url
    }
    
    func getData(completion: @escaping(Result<WeekData, DataError>) -> Void) {
        let dataTask = URLSession.shared.dataTask(with: self.url) { data, _, _ in
            guard let jsonData = data else {
                completion(.failure(.noDataAvailable))
                return
            }
            
            do {
                let jsonDecoder = JSONDecoder()
                let weekData = try jsonDecoder.decode(WeekData.self, from: jsonData)
                completion(.success(weekData))
            } catch {
                completion(.failure(.canNotProcessData))
            }
        }
        
        dataTask.resume()
    }
}

