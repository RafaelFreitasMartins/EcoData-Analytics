const fs = require('fs');
let html = fs.readFileSync('tema.html', 'utf8');

const newMain = 
        <main>
            <div class="header-title" style="text-align: center; margin-bottom: 40px;">
                <h1>Tema do Projeto</h1>
                <p>Agroclima Amazônia</p>
            </div>

            <div class="tema-grid">
                
                <div class="tema-card">
                    <h2>
                        <i class="ph-fill ph-globe-hemisphere-west"></i>
                        Impactos do El Niño e da La Niña na região Amazônica e em Belém (2014–2027)
                    </h2>
                    <p>Entre 2014 e 2027, a região Amazônica, com destaque para os estados do Amazonas e Pará e para os municípios de Manaus e Belém, apresenta forte relação entre a variabilidade climática associada aos fenômenos El Niño e La Niña, a disponibilidade hídrica, a produção agrícola, a navegação fluvial e os preços dos alimentos.</p>
                    <p>O El Niño tende a favorecer períodos de menor precipitação e temperaturas mais elevadas na Amazônia, aumentando o risco de estiagens, enquanto a La Niña pode favorecer condições mais úmidas em determinadas áreas, embora seus efeitos variem de acordo com a localização e com a interação entre o Oceano Pacífico e o Atlântico. O Ministério da Agricultura destaca que o Norte e a Amazônia estão entre as regiões brasileiras com maior risco de seca durante episódios de El Niño.</p>
                </div>

                <div class="tema-card" style="border-left-color: #3498db;">
                    <h2>
                        <i class="ph-fill ph-drop" style="color: #3498db;"></i>
                        Monitor Hidroclimático
                    </h2>
                    <p>O acompanhamento das condições climáticas e hidrológicas é fundamental para compreender esses impactos. Indicadores como precipitação, anomalia de precipitação, temperatura, nível dos rios e cota do Rio Negro no Porto de Manaus permitem identificar períodos de seca e cheia e antecipar seus efeitos sobre a população e as atividades econômicas.</p>
                    <p>Os episódios de El Niño de 2015–2016 e 2023–2024 se destacam pela intensidade dos impactos na Amazônia. Em 2024, por exemplo, a persistência do El Niño, combinada ao aquecimento anômalo do Atlântico, contribuiu para a manutenção de condições extremamente secas no Amazonas. O Rio Negro chegou a 12,11 metros em outubro de 2024, menor nível registrado em 122 anos de medições no Porto de Manaus.</p>
                </div>

                <div class="tema-card" style="border-left-color: #e67e22;">
                    <h2>
                        <i class="ph-fill ph-plant" style="color: #e67e22;"></i>
                        Vulnerabilidade Agrícola
                    </h2>
                    <p>A agricultura amazônica apresenta elevada vulnerabilidade às alterações no regime de chuvas porque grande parte da produção depende diretamente da disponibilidade natural de água e das condições do solo. Durante períodos de estiagem prolongada, a redução da umidade pode prejudicar o desenvolvimento das plantas, reduzir a produtividade e aumentar as perdas agrícolas.</p>
                    <p>Além disso, pequenos produtores, comunidades rurais e ribeirinhas são particularmente vulneráveis porque dependem simultaneamente da agricultura, dos rios e do transporte fluvial para produção, comercialização e abastecimento.</p>
                </div>

                <div class="tema-card" style="border-left-color: #8e44ad;">
                    <h2>
                        <i class="ph-fill ph-leaf" style="color: #8e44ad;"></i>
                        Impacto nas Culturas
                    </h2>
                    <p>Os efeitos climáticos não são iguais para todas as culturas. A mandioca, o milho e o feijão-caupi podem sofrer com o déficit hídrico, principalmente quando a falta de chuva ocorre em fases importantes do desenvolvimento das plantas. A Embrapa recomenda, para esses cultivos, o uso de variedades adaptadas, manejo adequado do solo e planejamento do período de plantio de acordo com a disponibilidade de água.</p>
                    <p>O açaí, especialmente nas áreas de várzea, também é sensível às alterações no nível dos rios. A redução prolongada das águas modifica as condições ambientais necessárias à produção, enquanto eventos extremos de cheia também podem afetar áreas agrícolas. Para o açaí produzido em terra firme, períodos de seca aumentam a necessidade de irrigação e de manejo da água.</p>
                    <p>O cacau também pode apresentar redução de produtividade quando ocorre déficit hídrico prolongado, principalmente em sistemas dependentes da regularidade das chuvas. Já a soja, cuja expansão ocorre principalmente em áreas agrícolas do Pará, apresenta maior exposição ao risco climático devido à necessidade de disponibilidade hídrica adequada durante diferentes fases do ciclo produtivo. Dessa forma, os efeitos combinados de seca, calor e alterações no calendário de chuvas podem aumentar as perdas e a instabilidade da produção.</p>
                </div>

                <div class="tema-card" style="border-left-color: #1abc9c;">
                    <h2>
                        <i class="ph-fill ph-boat" style="color: #1abc9c;"></i>
                        Gargalos Fluviais
                    </h2>
                    <p>Os impactos climáticos também ultrapassam o setor agrícola e atingem diretamente a logística amazônica. A redução da vazão dos rios dificulta a navegação de embarcações, aumenta o isolamento de comunidades ribeirinhas e pode interromper ou encarecer o transporte de alimentos, combustíveis, insumos agrícolas e outros produtos. Durante a seca de 2023, por exemplo, o nível do Rio Negro atingiu seu mínimo histórico em Manaus, afetando a navegação e a cadeia de suprimentos da Zona Franca.</p>
                    <p>Esse problema torna-se ainda mais relevante porque os rios funcionam como importantes corredores logísticos da Amazônia. Assim, uma redução significativa da cota do Rio Negro ou de outros rios estratégicos pode transformar um problema climático em um problema econômico e social, aumentando o tempo e o custo de transporte entre municípios produtores e centros consumidores.</p>
                </div>

                <div class="tema-card" style="border-left-color: #f1c40f;">
                    <h2>
                        <i class="ph-fill ph-coins" style="color: #f1c40f;"></i>
                        Preço dos Alimentos – Farinha de Mandioca
                    </h2>
                    <p>A combinação entre menor produção agrícola e maiores dificuldades logísticas pode refletir diretamente no preço dos alimentos. A farinha de mandioca, importante componente da alimentação regional, é um exemplo desse processo. Em períodos de seca, a redução da produção de mandioca pode diminuir a oferta do produto, enquanto os gargalos fluviais aumentam o custo de transporte. O resultado pode ser uma pressão sobre os preços tanto em Manaus quanto em Belém.</p>
                    <p>Em Manaus, esse efeito pode ser particularmente relevante devido à dependência do transporte fluvial e à distância em relação a diversas áreas produtoras. Já em Belém, apesar de possuir uma posição logística mais favorável e maior proximidade de importantes áreas produtoras do Pará, os efeitos climáticos sobre a produção também podem influenciar a disponibilidade e o preço da farinha. Dessa maneira, a comparação entre os preços de Farinha de Mandioca em Manaus e Farinha de Mandioca em Belém permite observar como as condições climáticas e logísticas podem gerar diferenças de preços entre os dois mercados.</p>
                </div>

                <div class="tema-card" style="border-left-color: #e74c3c;">
                    <h2>
                        <i class="ph-fill ph-calendar-blank" style="color: #e74c3c;"></i>
                        Perspectiva para 2026–2027
                    </h2>
                    <p>Para 2026–2027, o cenário merece atenção devido ao retorno do El Niño. O INMET informou em junho de 2026 que o fenômeno voltou a se estabelecer no Pacífico Equatorial e que a expectativa era de persistência até o final do verão austral de 2026/2027, podendo alcançar intensidade forte durante a primavera de 2026. O Serviço Geológico do Brasil também passou a reforçar o monitoramento hidrológico da Região Norte diante dos prognósticos de El Niño no segundo semestre de 2026.</p>
                    <p>Assim, 2014–2027 pode ser compreendido como um período marcado por significativa variabilidade hidroclimática, no qual os eventos de El Niño, especialmente 2015–2016 e 2023–2024, evidenciam a relação entre clima, disponibilidade hídrica e atividade econômica. A análise integrada do monitor hidroclimático, vulnerabilidade agrícola, produtividade das culturas, níveis dos rios, gargalos fluviais e preços da farinha de mandioca em Manaus e Belém permite demonstrar que os fenômenos climáticos não produzem apenas impactos ambientais: eles desencadeiam uma cadeia de efeitos que alcança a produção, a logística, o abastecimento e o custo dos alimentos na região Amazônica.</p>
                </div>
                
            </div>
        </main>
;

html = html.replace(/<main>[\s\S]*?<\/main>/g, newMain);
fs.writeFileSync('tema.html', html, 'utf8');
