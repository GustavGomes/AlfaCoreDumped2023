using System.ComponentModel.DataAnnotations;

namespace AlfaCoreDumped.Domain.Entities.ExternalCandidate
{
    public class Candidate
    {
        [Key]
        public Guid Id { get; set; }

        // Personal data

        [Required]
        public string CandidateName { get; set; }

        [Required]
        public string MotherName { get; set; }

        [Required]
        public string FatherName { get; set; }

        [Required]
        [RegularExpression("^[MFO]$", ErrorMessage = "Gender must be 'M', 'F', or 'O'.")]
        public char Genre { get; set; }

        [Required]
        public string CivilState { get; set; }

        [Required]
        public string EducationLevel { get; set; }

        [Required]
        public string Ethnicity { get; set; }

        // Birth Data
        [Required]
        public DateTime BirthDate { get; set; }

        [Required]
        public string Nacionality { get; set; }

        [Required]
        public string BirthCountry { get; set; }

        public string BirthState { get; set; }

        public string BirthCity { get; set; }

        // Sizes

        [Required]
        public string ShoeSize { get; set; }

        [Required]
        public string PantsSize { get; set; }

        [Required]
        public string ShirtSize { get; set; }

        // Contact
        [Required]
        public string TelephoneNumber { get; set; }

        public string SecondTelephoneNumber { get; set; }

        [Required]
        public string Email { get; set; }

        // Address
        [Required]
        public string Cep { get; set; }

        [Required]
        public string Country { get; set; }

        [Required]
        public string State { get; set; }

        [Required]
        public string City { get; set; }

        [Required]
        public string Neighborhood { get; set; }

        [Required]
        public string ResidencyType { get; set; }

        [Required]
        public string Street { get; set; }

        [Required]
        [Range(1, int.MaxValue)]
        public int ResidencyNumber { get; set; }

        public string Complement { get; set; }

        // Identification
        [Required]
        public string RgNumber { get; set; }

        [Required]
        public string RgEmissorOrg { get; set; }

        [Required]
        public string RgEmissorState { get; set; }

        [Required]
        public string RgEmissorCity { get; set; }

        [Required]
        public DateTime RgReleaseDate { get; set; }

        [Required]
        public string Cpf { get; set; }

        [Required]
        public string PisPasep { get; set; }

        // Others
        [Required]
        public string Function { get; set; }

        [Required]
        public string Lodged { get; set; }

        [Required]
        public string Pcd { get; set; }

        // Anexos

        [Required]
        public byte[] RgFile { get; set; }

        [Required]
        public byte[] CpfFile { get; set; }

        [Required]
        public byte[] ResumeFile { get; set; }

        public byte[] CnhFile { get; set; }

        public byte[] ArmyFile { get; set; }

        public bool HasFriendFamiliarWorking { get; set; }

        public ICollection<Relative> Relatives { get; set; }
            = new List<Relative>();

    }
}