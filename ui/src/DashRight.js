import React, { useState,useEffect } from 'react'
import { TagCloud } from 'react-tagcloud'
import './DashRight.css'
import ReactApexChart from 'react-apexcharts'
import axios from 'axios';
    
function DashRight() {
  const [wordspdata,setWordspdata] = useState({})

  // useEffect(() => {
  //   const sentimentCounter =[{"positive":"57.0"},{"negative":"22.0"},{"neutral":"21.0"}]
  //   sentimentCounter.map(sen=>console.log(sen))
    
  // }, [])
  
    

  const sentimentCounter = [{"value": "business", "count": 88}, {"value": "busy", "count": 54}, {"value": "blog", "count": 14}, {"value": "wordpress", "count": 8}, {"value": "seo", "count": 7}, {"value": "start", "count": 6}, {"value": "blogger", "count": 6}, {"value": "startup", "count": 6}, {"value": "new", "count": 6}, {"value": "like", "count": 5}, {"value": "work", "count": 5}, {"value": "could", "count": 4}, {"value": "u", "count": 4}, {"value": "use", "count": 4}, {"value": "forbidden", "count": 4}, {"value": "russian", "count": 4}, {"value": "help", "count": 4}, {"value": "mind", "count": 4}, {"value": "make", "count": 4}, {"value": "price", "count": 3}]
const sentimentCounter2 = [{"value": "football", "count": 97}, {"value": "footbal", "count": 64}, {"value": "fan", "count": 10}, {"value": "play", "count": 9}, {"value": "team", "count": 9}, {"value": "madrid", "count": 7}, {"value": "liverpool", "count": 7}, {"value": "final", "count": 7}, {"value": "real", "count": 6}, {"value": "ucl", "count": 6}, {"value": "call", "count": 6}, {"value": "man", "count": 6}, {"value": "best", "count": 6}, {"value": "player", "count": 5}, {"value": "leagu", "count": 5}, {"value": "get", "count": 5}, {"value": "heritag", "count": 4}, {"value": "game", "count": 4}, {"value": "watch", "count": 4}, {"value": "club", "count": 4}]

  const data={
    series: [57 ,22,21],
        options: {
          chart: {
            width: 380,
            type: 'pie',
          },
          labels: ['Positive', 'Negative', 'Neutral'],
          responsive: [{
            breakpoint: 480,
            options: {
              chart: {
                width: 200
              },
              legend: {
                position: 'bottom'
              }
            }
          }]
        },
      
}

const data3={
          
            series: [{
              data: [43,57]
            }],
            options: {
              chart: {
                type: 'bar',
                height: 350
              },
              plotOptions: {
                bar: {
                  borderRadius: 4,
                  horizontal: true,
                }
              },
              dataLabels: {
                enabled: false
              },
              xaxis: {
                categories: ['Negativity and neutral', 'Positive'
                ],
              }
            },
          
          
          };

  const data4 =  {
          
    series: [{
      name: 'series1',
      data: [31, 40, 28, 51, 42, 109, 100]
    }, {
      name: 'series2',
      data: [11, 32, 45, 32, 34, 52, 41]
    }],
    options: {
      chart: {
        height: 350,
        type: 'area'
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'smooth'
      },
      xaxis: {
        type: 'datetime',
        categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z"]
      },
      tooltip: {
        x: {
          format: 'dd/MM/yy HH:mm'
        },
      },
    },
  
  
  };
        

  return (
    <div className='DashRight'>

      <h1 className='Dashboard_head'>Welcome Aaqib<span>,xyz company</span></h1>
      <div className='Dashboard__top'>
        <div className='Dashboard__child'>
          <div  className='Dashboard__pie'>
            <ReactApexChart options={data.options} series={data.series} type="pie" width={380} />
          </div>
        </div>
        <div className='Dashboard__child1'>
        <ReactApexChart options={data3.options} series={data3.series} type="bar" height={350} />

        </div>
      </div>
      <div className='Dashboard__bottom'>
        <div className='Dashboard__child2'>
     
      <div className='DashRight__worldcloud'>
        
      <TagCloud
     minSize={20}
     maxSize={80}
     tags={sentimentCounter}
     onClick={tag => console.tag}
   />
        </div>
        </div>
        <div className='Dashboard__child21'>
        <ReactApexChart options={data4.options} series={data4.series} type="area" height={350} />

        </div>
      </div>
      
       
      
    </div>
     
  )
}

export default DashRight