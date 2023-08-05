import React, { useState } from "react";
import "./formCandidatos.css"
import { FormCheck } from "react-bootstrap";
const PersonForm = () => {
    const [person, setPerson] = useState({
        name: "",
        mother_name: "",
        father_Name: "",
        genre: "",
        civil_state: "",
        education_level: "",
        ethnicity: "",
        birth_Date: new Date(),
        nacionality: "",
        birth_country: "",
        birth_state: "",
        birth_city: "",
        shoe_size: 0,
        pants_size: 0,
        shirt_size: 0,
        telephone_number: "",
        second_telephone_number: "",
        email: "",
        cep: "",
        country: "",
        state: "",
        city: "",
        neighborhood: "",
        residency_type: "",
        street: "",
        residency_number: 0,
        complement: "",
        rg_number: "",
        rg_emissor_organ: "",
        rg_emissor_state: "",
        rg_emissor_city: "",
        rg_release_date: new Date(),
        cpf: "",
        pispasep: "",
        function: "",
        lodged: "",
        pcd: "",
    });



    const handleChange = (e) => {
        const { name, value } = e.target;
        setPerson((prevPerson) => ({ ...prevPerson, [name]: value }));
    };

    const [consentChecked, setConsentChecked] = useState(false);

    const handleConsentChange = (e) => {
        setConsentChecked(e.target.checked);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        test = {
            "id": 123,
            "candidateName": "John Doe",
            "motherName": "Jane Doe",
            "fatherName": "John Doe Sr.",
            "gender": "Male",
            "civiState": "Single",
            "educationLevel": "Bachelor's Degree",
            "ethnicity": "Caucasian",
            "birthDate": "1990-01-01",
            "nacionality": "American",
            "birthCountry": "United States",
            "birthState": "California",
            "birthCity": "Los Angeles",
            "shoeSize": "10",
            "pantsSize": "32",
            "shirtSize": "Medium",
            "telephoneNumber": "123-456-7890",
            "secondTelephoneNumber": "987-654-3210",
            "email": "john.doe@example.com",
            "cep": "12345-678",
            "country": "United States",
            "state": "California",
            "city": "San Francisco",
            "neighborhood": "Downtown",
            "residencyType": "Apartment",
            "street": "123 Main Street",
            "residencyNumber": 4,
            "complement": "Apartment complex",
            "rgNumber": "ABC12345",
            "rgEmissorCity": "Los Angeles",
            "rgReleaseDate": "2010-05-15",
            "cpf": "12345678901",
            "pispasep": "12345678900",
            "function": "Software Engineer",
            "lodged": true,
            "pcd": false,
            "rgFile": "base64_encoded_rg_file",
            "cpfFile": "base64_encoded_cpf_file",
            "resumeFile": "base64_encoded_resume_file",
            "cnhFile": "base64_encoded_cnh_file",
            "armyFile": "base64_encoded_army_file",
            "hasFriendFamiliar": true
        }
        
        responseJson ={
            "id": 123,
            "candidateName": person.name,
            "motherName": person.mother_name,
            "fatherName": person.father_Name,
            "gender": person.genre,
            "civiState": person.civil_state,
            "educationLevel": person.education_level,
            "ethnicity": person.ethnicity,
            "birthDate": person.birth_Date,
            "nacionality": person.nacionality,
            "birthCountry": person.birth_country,
            "birthState": person.birth_state,
            "birthCity": person.birth_city,
            "shoeSize": person.shoe_size,
            "pantsSize": person.pants_size,
            "shirtSize": person.shirt_size,
            "telephoneNumber": person.telephone_number,
            "secondTelephoneNumber": person.second_telephone_number,
            "email": person.email,
            "cep": person.cep,
            "country": person.country,
            "state": person.state,
            "city": person.city,
            "neighborhood": person.neighborhood,
            "residencyType": person.residency_type,
            "street": person.street,
            "residencyNumber": person.residency_number,
            "complement": person.complement,
            "rgNumber": person.rg_number,
            "rgEmissorCity": person.rg_emissor_city,
            "rgReleaseDate": person.rg_release_date,
            "cpf": person.cpf,
            "pispasep": person.pispasep,
            "function": person.function,
            "lodged": person.lodged,
            "pcd": person.pcd,
            "rgFile": person.rgFile,
            "cpfFile": person.cpfFile,
            "resumeFile": person.resumeFile,
            "cnhFile": person.cnhFile,
            "armyFile": person.armyFile,
            "hasFriendFamiliar": person.hasFriendFamiliar
        }

        fetch('https://localhost:5066/api/candidate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(responseJson),
        
        })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                console.log("Dados enviados com sucesso!")
            })
            .catch((error) => {
                console.error('Error:', error);
                console.log("Erro ao enviar dados!")
            });
        // Aqui você pode enviar os dados da pessoa para o servidor ou fazer outras ações necessárias com os dados
    };

    return (
        <div className="form-container">
            <h1 className="form--h1 text-center">Dados do candidato</h1>
            <p className="form--warning"><span className="bold">⚠️ ATENÇÃO:</span> o preenchimento dessas informações é de suma importância para o seu prosseguimento no processo seletivo. Todos os campos são
                OBRIGATÓRIOS, então se atente às informações preenchidas.</p>
            <form onSubmit={handleSubmit}>
                <div className="form--secao">
                    <div className="row">
                        <h3 className="form--titulo col-12">Dados Pessoais</h3>
                        <div className="form-group">
                            <p className="form--text"> Nome Completo:</p>
                            <label >
                                <input
                                    type="text"
                                    name="name"
                                    value={person.name}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>

                        <div className="form-group">
                            <p className="form--text">Nome Completo da Mãe:</p>
                            <label>
                                <input
                                    type="text"
                                    name="mother_name"
                                    value={person.mother_name}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>

                            <div className="form-group">
                                <p className="form--text">Nome Completo do Pai:</p>
                                <label>
                                    <input
                                        type="text"
                                        name="father_Name"
                                        value={person.father_Name}
                                        onChange={handleChange}
                                        className="input--form"
                                    />
                                </label>
                            </div>
                        </div>
                    </div>
                    <div className="row">
                        <div className="form-group col-md-3">
                            <p className="form--text">Sexo:</p>
                            <label>
                                <select name="genre" value={person.genre} onChange={handleChange}>
                                    <option value="homem">Homem</option>
                                    <option value="mulher">Mulher</option>
                                    <option value="ND">prefiro não responder</option>
                                </select>
                            </label>
                        </div>

                        <div className="form-group col-md-3">
                            <p className="form--text">Estado Civil:</p>
                            <label>
                                <select name="civil_state" value={person.civil_state} onChange={handleChange}>
                                    <option value="solteiro">Solteiro</option>
                                    <option value="casado">Casado</option>
                                    <option value="separado">Separado</option>
                                    <option value="divorciado">Divorciado</option>
                                    <option value="viúvo">Viúvo</option>
                                </select>
                            </label>
                        </div>

                        <div className="form-group col-md-3">
                            <p className="form--text">Grau:</p>
                            <label>
                                <select name="education_level" value={person.education_level} onChange={handleChange}>
                                    <option value="fundamental">Fundamental</option>
                                    <option value="medio">Medio</option>
                                    <option value="superior">Superior</option>
                                </select>
                            </label>
                        </div>

                        <div className="form-group col-md-3">
                            <p className="form--text">Raça/Cor:</p>
                            <label>
                                <select name="ethnicity" value={person.ethnicity} onChange={handleChange}>
                                    <option value="branca">Branca</option>
                                    <option value="preta">Preta</option>
                                    <option value="parda">Parda</option>
                                    <option value="amarela">Amarela</option>
                                    <option value="indigena">Indígena</option>
                                </select>
                            </label>
                        </div>
                    </div>

                </div>

                <div className="form--secao">
                    <div className="row">
                        <h3 className="form--titulo col-12">Dados de Nascimento</h3>
                        <div className="form-group col-md-4">
                            <p className="form--text">Data de Nascimento:</p> 
                            <label>
                                <input
                                    type="date"
                                    name="birth_Date"
                                    value={person.birth_Date}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>

                        <div className="form-group col-md-4">
                            <p className="form--text">Nacionalidade:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="nacionality"
                                    value={person.nacionality}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>

                        <div className="form-group col-md-4">
                            <p className="form--text">País de Nascimento:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="birth_country"
                                    value={person.birth_country}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                    </div>

                    <div className="row">
                        <div className="form-group col-md-6">
                            <p className="form--text">Estado de Nascimento:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="birth_state"
                                    value={person.birth_state}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                        <div className="form-group col-md-6">
                            <p className="form--text">Cidade de Nascimento:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="birth_city"
                                    value={person.birth_city}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                    </div>
                </div>

                <div className="form--secao">
                    <div className="row">
                        <h3 className="form--titulo col-12">Tamanhos</h3>
                        <div className="form-group col-md-4">
                            <p className="form--text">Botina:</p> 
                            <label>
                                <input
                                    type="number"
                                    name="shoe_size"
                                    value={person.shoe_size}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                        <div className="form-group col-md-4">
                            <p className="form--text">Número da Calça:</p> 
                            <label>
                                <input
                                    type="number"
                                    name="pants_size"
                                    value={person.pants_size}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                        <div className="form-group col-md-4">
                            <p className="form--text">Tamanho da Camisa:</p> 
                            <label>
                                <input
                                    type="number"
                                    name="shirt_size"
                                    value={person.shirt_size}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                    </div>
                </div>

                <div className="form--secao">
                    <div className="row">
                        <h3 className="form--titulo col-12">Contato</h3>
                        <div className="form-group col-md-6">
                            <p className="form--text">Telefone:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="telephone_number"
                                    value={person.telephone_number}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                        <div className="form-group col-md-6">
                            <p className="form--text">Telefone 02:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="second_telephone_number"
                                    value={person.second_telephone_number}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                    </div>
                </div>

                <div className="form--secao">
                    <div className="row">
                        <h3 className="form--titulo col-12">Endereço</h3>
                        <div className="form-group col-md-4">
                            <p className="form--text">CEP:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="cep"
                                    value={person.cep}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>

                        <div className="form-group col-md-4">
                            <p className="form--text">País:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="pais"
                                    value={person.pais}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>

                        <div className="form-group col-md-4">
                            <p className="form--text">Estado:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="state"
                                    value={person.state}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                    </div>

                    <div className="row">
                        <div className="form-group col-md-4">
                            <p className="form--text">Cidade:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="city"
                                    value={person.city}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>

                        <div className="form-group col-md-4">
                            <p className="form--text">Bairro:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="neighborhood"
                                    value={person.neighborhood}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>

                        <div className="form-group col-md-4">
                            <p className="form--text">Tipo de Logradouro:</p> 
                            <label>
                                <select name="ethnicity" value={person.residency_type} onChange={handleChange}>
                                    <option value="privado">Privado</option>
                                    <option value="publico">Público</option>
                                </select>
                            </label>
                        </div>
                    </div>

                    <div className="row">
                        <div className="form-group col-md-6">
                            <p className="form--text">Endereço Residencial:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="street"
                                    value={person.street}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>

                        <div className="form-group col-md-6">
                            <p className="form--text">Número:</p> 
                            <label>
                                <input
                                    type="number"
                                    name="residency_number"
                                    value={person.residency_number}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                    </div>

                    <div className="row">
                        <div className="form-group col-md-12">
                            <p className="form--text">Complemento:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="complement"
                                    value={person.complement}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                    </div>
                </div>


                <div className="form--secao">
                    <div className="row">
                        <h3 className="form--titulo col-12">Carteira de Identidade, CPF e PIS</h3>
                    </div>

                    <div className="row">
                        <div className="form-group col-md-6">
                            <p className="form--text">Número da Carteira de Identidade:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="rg_number"
                                    value={person.rg_number}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>

                        <div className="form-group col-md-6">
                            <p className="form--text">Orgão Emissor da Carteira de Identidade:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="rg_emissor_organ"
                                    value={person.rg_emissor_organ}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                    </div>

                    <div className="row">
                        <div className="form-group col-md-6">
                            <p className="form--text">Estado de Emissão da Identidade (RG)*:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="rg_emissor_state"
                                    value={person.rg_emissor_state}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>

                        <div className="form-group col-md-6">
                            <p className="form--text"> Cidade de Emissão da Identidade (RG):</p> 
                            <label>
                                <input
                                    type="text"
                                    name="rg_emissor_city"
                                    value={person.rg_emissor_city}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                    </div>

                    <div className="row">
                        <div className="form-group col-md-6">
                            <p className="form--text">Data de Expedição da Identidade (RG):</p> 
                            <label>    
                                <input
                                    type="date"
                                    name="rg_release_date"
                                    value={person.rg_release_date}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>

                        <div className="form-group col-md-6">
                            <p className="form--text">CPF:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="cpf"
                                    value={person.cpf}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                    </div>

                    <div className="row">
                        <div className="form-group col-md-6">
                            <p className="form--text">PIS/PASEP:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="pispasep"
                                    value={person.pispasep}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>
                    </div>
                </div>


                <div className="form--secao">
                    <div className="row">
                        <h3 className="form--titulo col-12">Outros</h3>
                    </div>

                    <div className="row">
                        <div className="form-group col-md-4">
                            <p className="form--text">Função:</p> 
                            <label>
                                <input
                                    type="text"
                                    name="function"
                                    value={person.function}
                                    onChange={handleChange}
                                    className="input--form"
                                />
                            </label>
                        </div>

                        <div className="form-group col-md-4">
                            <p className="form--text">Alojado:</p> 
                            <label>
                                <select name="lodged" value={person.lodged} onChange={handleChange}>
                                    <option value="sim">Sim</option>
                                    <option value="não">Não</option>
                                </select>
                            </label>
                        </div>

                        <div className="form-group col-md-4">
                            <p className="form--text">PCD:</p>
                            <label>
                                <select name="pcd" value={person.pcd} onChange={handleChange}>
                                    <option value="sim">Sim</option>
                                    <option value="não">Não</option>
                                    <option value="ND">prefiro não responder</option>
                                </select>
                            </label>
                        </div>
                    </div>
                </div>

                <div className="form--secao">
                    <h3 className="form--titulo">Dependentes</h3>
                </div>

                <div className="form--declaracao">
                    <label>
                        <input
                            className="form--check"
                            type="checkbox"
                            checked={consentChecked}
                            onChange={handleConsentChange}
                        />
                        Declaro ciente de que a coleta dos meus dados aqui solicitados é essencial para me candidatar às vagas ofertadas pela empresa, sendo que autorizo
                        expressamente à ALFA ENGENHARIA, neste ato, a coletar, armazenar e utilizar meus dados para esta finalidade. Declaro ciente ainda de que a
                        empresa encontra-se adequada à Lei Geral de Proteção de Dados, de forma que tive acesso à Política de Privacidade, publicada no site.
                    </label>
                </div>

                <div className="text-center">
                    <button className="btn" type="submit">Enviar</button>
                </div>

            </form>
        </div>
    );
};

export default PersonForm;
