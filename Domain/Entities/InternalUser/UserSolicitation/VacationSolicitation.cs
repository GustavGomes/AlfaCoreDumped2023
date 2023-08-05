using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AlfaCoreDumped.Domain.Entities.InternalUser.UserSolicitation
{
    public class VacationSolicitation
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        [ForeignKey("CreatorUser")]
        public Guid CreatorUserId { get; set; }

        [Required]
        [ForeignKey("TargetUser")]
        public Guid TargetUserId { get; set; }

        public User CreatorUser { get; set; }

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
