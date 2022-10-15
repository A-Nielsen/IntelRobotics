<template>
  <div class="banner lighter headerlarge">Our history</div>
  
  <div class="banner lighter header">Indledning</div>
  <div class="banner lighter ">
    <p>
    Denne afsluttende rapport lavet af Asger Nielsen, Mikkel Rahbek Christensen og Marcus Meyer Bertelsen, omhandler EUX faget Informatik B.  

    Asger og Mikkel er datateknikere med speciale i programmering, mens Marcus er datatekniker med special i infrastruktur. Sammen har vi udviklet to produkter, en hjemmeside samt Restful Application Programming Interface (API) og et windows domæne, som skal udgøre infrastrukturen for det fiktionelle firma IntelRobotics. 

    Problemstillingen for opgaven er at firmaet IntelRobotics er I udvikling. De opkøber to industrifirmaer is Japan og Italien. Derfor ønsker IntelRobotics en ny løsning til deres IT struktur, som skal sikre effektivt arbejde i, og imellem de nye afdelinger. Sikkerhed skal der tages højde for, og da to af afdelingerne ligger I EU-lande, skal GDPR derfor også tænkes ind i løsningen. 
    </p>
  </div>
  <div class="banner lighter header">Problembeskrivelse</div>
  <div class="banner lighter ">
    <p>
      Firmaet IntelRobotics har opkøbt to industrifirmaer i Japan og Italien. Virksomheden har nu 120 medarbejdere som skal administreres og som skal samarbejde, derfor ønsker ledelsen en omstrukturering af IT systemerne. 

      Danmark, Italien og Japan har salgsafdelinger. Japan og Danmark har samtidigt produktions afdelinger. Alle lande har en Administrations- og IT afdeling. 

      Ledelsen ønsker en domæne baseret infrastruktur til administration af virksomhedens nye ressourcer. Sikkerhed er vigtigt og der skal derfor tages skarpt hensyn til opsætningen. Både mellem de forskellige afdelinger, og lokalt. 

      Samtidigt ønsker ledelsen en ny hjemmeside, med informationer om virksomheden og virksomhedens produkter.  

      Altså er der to opgaver: 

      Domæne til alle afdelinger 

      Hjemmeside 
      </p>
  </div>

</template>

<style scoped>
  .headerlarge{
    padding: 40px;
    margin:0;
  }
    .header{
      margin:0;
    }
    p{
      max-width: 40vw;
      margin: var(--margin-default);
  } 
    
  @media only screen and (max-width: 1024px) {
    p{
    max-width: 80vw;
    }
  }
</style>