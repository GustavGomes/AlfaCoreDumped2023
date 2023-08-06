import React, { useState } from "react";
import "./formCandidatos.css"
import axios from 'axios';
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
        cnh_file: "",
        has_friend_familiar: "",
    });



    const handleChange = (e) => {
        const { name, value } = e.target;
        setPerson((prevPerson) => ({ ...prevPerson, [name]: value }));
    };

    function handleFileChange(e) {
        setFile(e.target.files[0])
    }

    const [consentChecked, setConsentChecked] = useState(false);

    const handleConsentChange = (e) => {
        setConsentChecked(e.target.checked);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (consentChecked) {
            // Realize as ações necessárias com o consentimento concedido
            console.log('Consentimento concedido!');

            // Realizar a requisição ao servidor
            fetch("http://192.168.5.184:5066/api/insertCandidate", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(person),
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log("Resposta do servidor:", data);
                })
                .catch((error) => {
                    console.error("Erro ao enviar os dados:", error);
                });

            const url = 'http://192.168.5.184:5066/api/uploadFile';
            // const formData = new FormData();
            // formData.append('file', file);
            // formData.append('fileName', file.name);
            // const config = {
            //     headers: {
            //         'content-type': 'multipart/form-data',
            //     },
            // };
            // axios.post(url, formData, config).then((response) => {
            //     console.log(response.data);
            // });
            base64File = ''
            reader = new FileReader();
            reader.onload = function(event) {
                const base64String = event.target.result.split(',')[1];
                base64File = base64String;
            }
            // Realiza a requisição ao servidor
            fetch("http://192.168.5.184:5066/api/uploadFile", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    'cpf': person.cpf,
                    'fileName': file.name,
                    'type': file.type.split('/')[1],
                    '64base': base64File
                }),
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log("Resposta do servidor:", data);
                })
                .catch((error) => {
                    console.error("Erro ao enviar os dados:", error);
                });

        } else {
            console.error('O consentimento é obrigatório!');
        }
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
                    <h3 className="form--titulo">Anexar Documento</h3>
                    <div className="row">
                        <div className="form-group col-12">
                            <input type="file" accept=".pdf" className="input--form" onChange={handleFileChange} />
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
