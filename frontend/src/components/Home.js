import React, { useState } from 'react';
import '../styles/Home.css';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import UploadIcon from '@mui/icons-material/Upload';

export const Home = ({setResult, imgUrl, setImgUrl}) => {
    const [ loading, setLoading ] = useState(false);
    const navigate = useNavigate();
    const [file, setFile] = useState(null);
    async function handleSubmit (e) {
        e.preventDefault();
        setLoading(true);
        try{
            const formData = new FormData();
            formData.append('file', file);
            const result = await axios.post("http://127.0.0.1:4200/predict", formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            console.log(result)
            setResult(result.data)
            setLoading(false);
            navigate('/result');
        }catch(err){
            console.log(err);
            setLoading(false);
        }
    }
    function handleChange(e){
        setFile(e.target.files[0]);
        const url=URL.createObjectURL(e.target.files[0]);
        setImgUrl(url);
    }
    return(
        <div id='home'>
        {loading?(<h3>Loading...</h3>):(
            <>
            <div>
                <h2>Choose the image you wish to check</h2>
                <form id='input-form' onSubmit={handleSubmit}>
                    <label id='input-label' htmlFor='file-input'>Upload image <UploadIcon/></label>
                    <input id='file-input' type="file" name="file" accept="image/*" onChange={handleChange}/>
                    <button id='submit-btn' type="submit">Check</button>
                </form>
            </div>
            {imgUrl&&(<img src={imgUrl} alt='uploaded image' height="250" width="250"/>)}
            </>)}
        </div>
    )
}