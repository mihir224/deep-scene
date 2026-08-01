import React from 'react';
import '../styles/Result.css';
import {Navigate} from 'react-router-dom';

export const Result = ({result, imgUrl}) => {
    return(
        <div>
       {!result?(<Navigate to='/' replace={true}/>)
            :(<div id='result'>
                {imgUrl&&(<img src={imgUrl} alt='uploaded image' height="250" width="250"/>)}
                <div>
                    <h1>Result</h1>
                    <p className='result-text'>This image is {result.result==='Deepfake'?'a':''} <span style={{color:result.result==='Deepfake'?'red':'green', fontWeight:'bold'}}>{result.result}</span>!</p>
                    <p className='result-text' >Predicted likelihood: {result.predicted_class?.toFixed(7)}</p>
                    <div >
                        <p id='info'>*PL near 0 = Deepfake & near 1 = Real </p>
                    </div>
                </div>
            </div>)
            }
        </div>
    )
}