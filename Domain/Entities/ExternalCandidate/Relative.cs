using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AlfaCoreDumped.Domain.Entities.ExternalCandidate
{
    public class Relative
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        public Guid CandidateId { get; set; }

        [ForeignKey("CandidateId")]
        [Required]
        public Candidate Candidate { get; set;}

        [Required]
        public string Cpf { get; set; }

        [Required]
        public string Name { get; set; }

        [Required]
        public string Kinship { get; set; }

        [Required]
        public DateTime Birthday { get; set; }
    }
}
