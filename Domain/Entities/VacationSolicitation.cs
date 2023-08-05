using System.ComponentModel.DataAnnotations;

namespace AlfaCoreDumped.Domain.Entities
{
    public class VacationSolicitation
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        public User CreatorUser { get; set; }

        [Required]
        public User TargetUser { get; set; }

        [Required]
        public string Status { get; set; }

        [Required]
        public DateTime VacationStartDate { get; set; }

        [Required]
        public DateTime VacationEndDate { get; set; }

        public string Description { get; set; }

        public DateTime CreationDate { get; set; }

        public DateTime StartDate { get; set; }

        public DateTime EndDate { get; set; }
    }
}
